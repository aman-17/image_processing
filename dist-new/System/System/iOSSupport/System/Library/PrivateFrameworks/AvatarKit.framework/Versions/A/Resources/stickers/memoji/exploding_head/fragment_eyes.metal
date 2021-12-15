float offset = 3.1;
float3 point = (scn_node.inverseModelViewTransform * float4(_surface.position.xyz, 1.0)).xyz;

float mask1 = saturate(point.z/10);
mask1 = step(0.758, mask1);

float mask2 = 1.0-saturate((point.y - 4) / 13.5);
mask2 = step(0.31, mask2);

if (mask1 * mask2<0.9) discard_fragment();
