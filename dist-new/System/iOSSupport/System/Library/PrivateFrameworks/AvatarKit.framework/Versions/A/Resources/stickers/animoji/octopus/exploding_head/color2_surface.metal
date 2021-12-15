_surface.diffuse = pow(float4(0.764, 0.338, 0.408, 1.0), 2.3);
_surface.emission = pow(float4(0.611, 0.271, 0.314, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.446, 0.055, 0.0, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.5, 2, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.5, 0.0, 0.0, 0.0);
