# setup
https://ubuntu.com/blog/getting-started-with-flutter-on-ubuntu

# Main Instructions


# create app
mkdir flutter_example
cd flutter_example

flutter create .

flutter run -d linux


# create build 
we need to sign the app, configure min sdk version (according to minimum android os we want to support in our app), and add keystore

## sign the app
```
keytool -genkey -v -keystore <your_keystore_name>.jks -keyalg RSA -keysize 2048 -validity 10000 -alias <your_alias_name>
```
Replace <your_keystore_name> with your desired keystore filename (e.g., key.jks).
Replace <your_alias_name> with an alias (e.g., my-key-alias).
You'll be prompted to set a password and other details.


properly configure below files from goal tracker app
```
goal_tracker/android/key.properties # need to be generated - containing key information we created
goal_tracker/android/gradle.properties
<!-- goal_tracker/android/app/build.gradle  -->
goal_tracker/android/app/build.gradle    # android version and generated key details need to be configured
```

Export path if needed
export FLUTTER_ROOT="/home/vis/snap/flutter/common/flutter"

Create Build
flutter build apk --release --split-per-abi # command to build apk

# keep in mind
- there are two android/build.gradle and android/app/build.gradle
- To update to the latest version, run "flutter upgrade". 

# to run app after solving error
flutter clean
flutter pub get
flutter run -d linux # this is sufficient



# refenrece
https://chatgpt.com/c/66efdbb9-7fe4-8012-ab2c-ff551f52bfb5

- solve exceptions
- it should scan all the music and able to play
- in android - it is not showing icons on bottom

