_surface.diffuse = pow(float4(0.576, 0.514, 0.494, 1.0), 2.3);
_surface.emission = pow(float4(0.451, 0.384, 0.373, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.446, 0.177, 0.005, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.185, 2.322, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 0.9, 0.9, 1.0);
// Wrap
_surface.specular = float4(0.333, 1.246, -5.86, 0.0);
