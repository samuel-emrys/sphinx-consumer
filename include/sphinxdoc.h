#pragma once

#ifdef _WIN32
  #define sphinxdoc_EXPORT __declspec(dllexport)
#else
  #define sphinxdoc_EXPORT
#endif

sphinxdoc_EXPORT void sphinxdoc();
