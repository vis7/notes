# shutil

copy(source, destination, *, follow_symlinks = True) - copy source file to destination

copy2(source, destination, *, follow_symlinks = True) - same as copy(), but try to preserve file's metadata

copytree() - this method recursively copies an entire directory tree rooted at source (src) to the destination directory. The destination directory, named by (dst) must not already exist. It will be created during copying.


rmtree() is used to delete an entire directory tree, the path must point to a directory (but not a symbolic link to a directory).

which() - method tells the path to an executable application that would be run if the given cmd was called. This method can be used to find a file on a computer which is present on the PATH.

```
# importing shutil module 
import shutil 
   
# file search 
cmd = 'anaconda'
   
# Using shutil.which() method
locate = shutil.which(cmd)
   
# Print result
print(locate)
````