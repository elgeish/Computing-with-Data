# Ant

```xml
<?xml version="1.0"?>
<project name="hello" default="build">
  <target name="build" description="build project">
    <mkdir dir="classes"/>
    <javac destdir="classes">
      <src path="src"/>
    </javac>
  </target>
  <target name="clean" description="clean class files">
    <delete>
      <fileset dir="classes">
        <include name="*.class"/>
      </fileset>
    </delete>
  </target>
</project>
```
