[fabrician.org](http://fabrician.org/) - Maven Archetypes
==========================================================================

Introduction
--------------------------------------
This project includes a set of Maven Archetypes for starting Fabrician projects.

To use these archetypes you simply install them.

```bash
mvn install
```


Enabler Archetype
--------------------------------------
The Enabler Archetype creates a simple project for developing a custom TIBCO Silver Fabric Enabler.

```bash
mvn archetype:generate -DarchetypeGroupId=org.fabrician -DarchetypeArtifactId=enabler-archetype -DarchetypeVersion=1.1 -DgroupId=my.groupId -DartifactId=myArtifactId
```

Custom Rule Condition Archetype
--------------------------------------
The Condition Archetype creates a simple project for developing a custom TIBCO Silver Fabric Custom Rule Condition.

```bash
mvn archetype:generate -DarchetypeGroupId=org.fabrician -DarchetypeArtifactId=condition-archetype -DarchetypeVersion=1.1 -DgroupId=my.groupId -DartifactId=myArtifactId
```
