    path('admin/', admin.site.urls),
    path('api/', include('LittleLemonAPI.urls', namespace='littlelemonapi')),
    path('api/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))