_surface.diffuse = pow(float4(0.564, 0.382, 0.243, 1.0), 1.7);
_surface.emission = pow(float4(0.348, 0.202, 0.086, 1.0), 1.7);
// EdgesDarkeningColor
_surface.ambient = float4(1.0, 1.0, 1.0, 1.0);
// edgeDark_rimLight
_surface.reflective = float4(0, 0, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 0.7, 0.3, 1.0);
// Wrap
_surface.specular = float4(0.5, 0.2, -8, 0.0);
