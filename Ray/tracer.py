from Ray import ray
from Obj import obj
import config

class Tracer:
    def __init__(self):
        self.ray_list = []
        for x in range(config.xlim):
            for y in range(config.ylim):
                ray0 = ray.Ray(x - 250,y - 205,0,config.view_x,config.view_y,config.view_z,x,y)
                #ray0.normalize()
                self.ray_list.append(ray0)
                self.y += 1
    def test(self,obj,layer):
            # // intersect3D_RayTriangle(): find the 3D intersection of a ray with a triangle
            # //    Input:  a ray R, and a triangle T
            # //    Output: *I = intersection point (when it exists)
            # //    Return: -1 = triangle is degenerate (a segment or point)
            # //             0 =  disjoint (no intersect)
            # //             1 =  intersect in unique point I1
            # //             2 =  are in the same plane
            intersect3D_RayTriangle( Ray R, Triangle T, Point* I ){
            #Vector    u, v, n;              // triangle vectors
            Vector    dir, w0, w;           // ray vectors
            float     r, a, b;              // params to calc ray-plane intersect

            // get triangle edge vectors and plane normal
            u = obj.cord[1] - obj.cord[0]#V1 - V0;
            v = obj.cord[2] - obj.cord[0] #V2 - T.V0;
            n = u * v;              // cross product
            if (n == (Vector)0)             // triangle is degenerate
                return -1;                  // do not deal with this case

            dir = R.P1 - R.P0;              // ray direction vector
            w0 = R.P0 - T.V0;
            a = -dot(n,w0);
            b = dot(n,dir);
            if (fabs(b) < SMALL_NUM) {     // ray is  parallel to triangle plane
                if (a == 0)                 // ray lies in triangle plane
                    return 2;
                else return 0;              // ray disjoint from plane
            }

            // get intersect point of ray with triangle plane
            r = a / b;
            if (r < 0.0)                    // ray goes away from triangle
                return 0;                   // => no intersect
            // for a segment, also test if (r > 1.0) => no intersect

            *I = R.P0 + r * dir;            // intersect point of ray and plane

            // is I inside T?
            float    uu, uv, vv, wu, wv, D;
            uu = dot(u,u);
            uv = dot(u,v);
            vv = dot(v,v);
            w = *I - T.V0;
            wu = dot(w,u);
            wv = dot(w,v);
            D = uv * uv - uu * vv;

            // get and test parametric coords
            float s, t;
            s = (uv * wv - vv * wu) / D;
            if (s < 0.0 || s > 1.0)         // I is outside T
                return 0;
            t = (uv * wu - uu * wv) / D;
            if (t < 0.0 || (s + t) > 1.0)  // I is outside T
                return 0;

            return 1;                       // I is in T
        }
