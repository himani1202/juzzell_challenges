a 3-tier web application gets deployed using helm charts.
this web application consist of apache as a web interface, tomcat as a web server where a java application is running and redis as a storage backend.
All the pods get created nder one kubernetes namespace
Service type of apache is kept as Loadbalancer so that the pods interact with outside world.
The tomcat and apache pods gets horizontally scaled upto 5 pods as soon as the CPU utilization on these pods reach 90 percent.