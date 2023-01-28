#include <assert.h>
#include <stdlib.h>

typedef struct rect {
   float xdim;
   float ydim;
} Rect;

Rect* makerect(float x, float y) {
   Rect* r = (Rect*) malloc(sizeof(Rect));
   r->xdim = x;
   r->ydim = y;
   return r;
}

float area(Rect* r) {
   return r->xdim * r->ydim;
}

int main() {
   Rect* r = makerect(2.0, 4.0);
   float a = area(r);
   assert(a == 8.0);
   free(r);
   return 0;
}

