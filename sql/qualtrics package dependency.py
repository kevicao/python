





# Q: https://odo.corp.qualtrics.com/wiki/index.php/Interviewing/Brontosaurus/FindDependencyConflicts
# Software today rarely implements everything needed from scratch. It depends on other open source or internally developed software, which in turn depends on other software. Having two or more versions of the same software library in one project can cause strange behavior so we’d like to identify such situations ahead of time.

# Given the Package object definition below, find and report any Package version conflicts that exist in its dependencies. A conflict is defined as two or more versions of a dependent package that have different versions. Return the Package names and versions for any and all conflicts.

class Package:
  def __init__(self, name, version):
    self.name = name
    self.version = version
    self.dependencies = []

  def add_dependency(self, package):
    self.dependencies.append(package)
# Example:
#                         /---- D(1.0)
#                         |
#         /---    B(1.0)  
#         |               |                 /---- F(1.0)
#         |               \---- E(1.0)
#         |
# A(1.0)  
#         |               /---- D(1.0)
#         |               |
#         \---    C(1.0)
#                         |                 /---- F(1.1)
#                         \---- E(2.0)

# Package: E Versions: 1.0, 2.0
# Package: F Versions: 1.0, 1.1

def find_conflicts(package):
    h = {}
    
    queue = [package]
    while queue:
        tmp = []
        for pack in queue:
            if pack.name in h:
                if pack.version not in h[pack.name]:
                    h[pack.name].append(pack.version)
            else:
                h[pack.name] = [pack.version]
            
            tmp = tmp + pack.dependencies
        queue = tmp[:]
    

    for key in h:
        if len(h[key]) > 1:
            print(key, h[key])
            
    
a = Package('A', '1.0')
b = Package('B', '1.0')
e = Package('E', '1.0')
e2 = Package('E', '2.0')
c = Package('C', '1.0')
d = Package('D', '1.0')
a.add_dependency(b)
a.add_dependency(c)
b.add_dependency(e)
b.add_dependency(d)

c.add_dependency(d)
d.add_dependency(e2)

find_conflicts(a)
                h[pack.name] = [pack.version]
            