# setup
https://ubuntu.com/blog/getting-started-with-flutter-on-ubuntu

# create app
mkdir flutter_example
cd flutter_example

flutter create .

flutter run -d linux


# create build 
we need to sign the app, configure min sdk version (according to minimum android os we want to support in our app), and add keystore

properly configure below files from goal tracker app
goal_tracker/android/key.properties
goal_tracker/android/gradle.properties
goal_tracker/android/app/build.gradle 


flutter build apk --release --split-per-abi # command to build apk


# refenrece
https://chatgpt.com/c/66efdbb9-7fe4-8012-ab2c-ff551f52bfb5

