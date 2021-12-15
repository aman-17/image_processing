_surface.diffuse = pow(float4(0.431, 0.310, 0.173, 1.0), 2.3);
_surface.emission = pow(float4(0.251, 0.169, 0.082, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.429, 0.286, 0.000, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(1.1, 3, 0, 0);
// SpecularColor
_surface.multiply = float4(0.2, 0.2, 0.2, 1.0);
// Wrap
_surface.specular = float4(0.6, 0.6, -7.0, 0.0);
