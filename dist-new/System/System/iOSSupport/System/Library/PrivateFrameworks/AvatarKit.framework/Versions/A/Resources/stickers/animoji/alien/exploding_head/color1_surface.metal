_surface.diffuse = pow(float4(0.451, 0.522, 0.525, 1.0), 2.3);
_surface.emission = float4(0.0, 0.0, 0.0, 1.0);
// EdgesDarkeningColor
_surface.ambient = float4(1.0, 1.0, 1.0, 1.0);
// edgeDark_rimLight
_surface.reflective = float4(0, 0, 0.8, 4);
// SpecularColor
_surface.multiply = float4(1.05, 1.2, 1.2, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, 0.0, 0.0);
