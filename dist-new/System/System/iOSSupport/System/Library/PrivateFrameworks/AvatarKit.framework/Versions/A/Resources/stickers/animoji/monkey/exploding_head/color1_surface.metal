_surface.diffuse = pow(float4(0.713, 0.581, 0.372, 1.0), 2.3);
_surface.emission = pow(float4(0.216, 0.169, 0.067, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.615, 0.418, 0.173, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.5, 3, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, 0.0, 0.0);
