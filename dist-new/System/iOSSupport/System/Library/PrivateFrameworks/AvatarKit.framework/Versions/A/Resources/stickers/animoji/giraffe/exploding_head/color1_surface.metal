_surface.diffuse = pow(float4(0.788, 0.569, 0.278, 1.0), 2.3);
_surface.emission = pow(float4(0.717, 0.522, 0.259, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.700, 0.532, 0.245, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.5, 3, 0.009, 10);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, 0.0, 0.0);
