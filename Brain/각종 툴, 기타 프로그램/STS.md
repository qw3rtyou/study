
# Troubleshoot
### An error has occurred. See error log for more details.java.lang.ExceptionInInitializerError
- STS.ini
```xml
-startup
plugins/org.eclipse.equinox.launcher_1.6.300.v20210813-1054.jar
--launcher.library
plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.2.300.v20210828-0802
-product
org.springsource.sts.ide
--launcher.defaultAction
openFile
-vm
C:\Program Files\Java\jdk-11\bin\javaw.exe
-vmargs
-Dosgi.requiredJavaVersion=11
-Dosgi.dataAreaRequiresExplicitInit=true
-Xms256m
-Xmx2048m
--add-modules=ALL-SYSTEM
-Dosgi.module.lock.timeout=10

```



