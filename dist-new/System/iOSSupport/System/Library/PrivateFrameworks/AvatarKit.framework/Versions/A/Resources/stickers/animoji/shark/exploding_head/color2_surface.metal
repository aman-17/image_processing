_surface.diffuse = pow(float4(0.679, 0.706, 0.725, 1.0), 2.3);
_surface.emission = pow(float4(0.565, 0.603, 0.627, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.500, 0.503, 0.506, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.4, 3, 0.1, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.63, 10, 0.0);
