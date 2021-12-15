_surface.diffuse = pow(float4(0.769, 0.744, 0.788, 1.0), 2.3);
_surface.emission = pow(float4(0.443, 0.399, 0.435, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.139, 0.140, 0.135, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(1, 2, 1, 10);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.5, 1.0, 0.0, 0.0);
