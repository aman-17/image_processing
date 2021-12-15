_surface.diffuse = pow(float4(0.412, 0.419, 0.427, 1.0), 2.3);
_surface.emission = pow(float4(0.349, 0.357, 0.361, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.500, 0.503, 0.506, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.4, 3, 0.1, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.63, 10, 0.0);
