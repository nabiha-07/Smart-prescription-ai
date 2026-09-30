# STEP 1 — Create the Android Studio Project (Java + XML)

> Project: **Smart Prescription Assistant BD**
> Package: `com.example.smartprescriptionassistantbd`
> Language: **Java only** · UI: **XML Views only** · **No Kotlin app code, no Jetpack Compose**

---

## 1. What we are building in this step

Nothing functional yet. In this step we only create the **empty Android Studio project shell** that
every later step will build on top of:

- a Gradle project named `Smart Prescription Assistant BD`
- an application id / package `com.example.smartprescriptionassistantbd`
- one Java activity (`MainActivity.java`)
- one XML layout (`activity_main.xml`)
- an `AndroidManifest.xml`

By the end of this step you must be able to press **Run ▶** and see a blank screen with the text
`Hello World!` on an emulator or a real phone.

## 2. Why we are building it

If the project is created with the **wrong template**, Android Studio will generate **Kotlin files
and Jetpack Compose UI**, and everything in the remaining 23 steps will fail to compile or will not
match the instructions. The single most important decision in this whole project is made in this
step: choosing **Empty Views Activity** + **Java** + **Groovy DSL**.

---

## 3. Exact Android Studio clicks

### 3.1 Open the new-project wizard

1. Launch **Android Studio**.
2. On the Welcome screen click **New Project**.
   *(If a project is already open instead: menu **File → New → New Project…**)*

### 3.2 Choose the template — THE MOST IMPORTANT SCREEN

You will see a screen titled **New Project** with a list of templates on the left
(`Phone and Tablet`, `Wear OS`, `Television`, ...) and template tiles on the right.

1. In the left column, select **Phone and Tablet**.
2. In the tile list, scroll and select **Empty Views Activity**.
3. Click **Next**.

> ⚠️ **CRITICAL — read this twice**
>
> | Template tile | What it generates | Use it? |
> |---|---|---|
> | **Empty Views Activity** | Java/Kotlin + **XML layouts** | ✅ **THIS ONE** |
> | **Empty Activity** | Kotlin + **Jetpack Compose** | ❌ NO |
> | **Basic Views Activity** | XML but adds Navigation component + fragments | ❌ NO (too complex) |
> | **No Activity** | Nothing at all | ❌ NO |
>
> In Android Studio Giraffe and newer, the tile simply called **"Empty Activity"** is the
> **Compose** template. The one with the word **"Views"** in it is the XML one. If your tile list
> does not contain "Empty Views Activity", your Android Studio is very old — tell me your version
> and I will adjust.

### 3.3 Fill in the project details screen

Fill each field **exactly** as follows:

| Field | Value to type / select |
|---|---|
| **Name** | `Smart Prescription Assistant BD` |
| **Package name** | `com.example.smartprescriptionassistantbd` |
| **Save location** | anywhere you like, e.g. `C:\AndroidProjects\SmartPrescriptionAssistantBD` |
| **Language** | **Java** ← select from the dropdown |
| **Minimum SDK** | `API 24 ("Nougat"; Android 7.0)` *(see note below)* |
| **Build configuration language** | **Groovy DSL (build.gradle)** |

Then click **Finish**.

**Notes on the fields**

- **Name** — type it with the spaces exactly as shown. Android Studio will show
  `Smart Prescription Assistant BD` as the app label and will put it in `settings.gradle` as
  `rootProject.name`. The folder it creates will be `SmartPrescriptionAssistantBD` (spaces removed) —
  that is normal and correct.
- **Package name** — Android Studio may auto-fill something like
  `com.example.smartprescriptionassistantbd` already (it lowercases and strips spaces from the Name).
  **Verify it character by character.** If it is different, click into the field and correct it.
  A wrong package name means every `import` and every `<activity>` entry in the rest of this project
  will be wrong.
- **Language: Java** — if this dropdown is missing or greyed out, you selected the Compose template.
  Go **Back** and pick **Empty Views Activity**.
- **Minimum SDK** — `API 24` is a safe default: ML Kit Text Recognition requires API 21+, and API 24
  covers roughly 97% of devices. If you have a specific requirement, tell me and I will use yours.
- **Build configuration language: Groovy DSL (build.gradle)** — Android Studio Hedgehog and newer
  default this to **Kotlin DSL (build.gradle.kts)**. Change it to **Groovy DSL**.

  > To be precise and honest: `build.gradle.kts` is a *build script*, not Android app code — it would
  > not put Kotlin into your app. But every Java Android tutorial, and every snippet I give you in
  > Step 2, uses the Groovy `build.gradle` syntax. Choosing Groovy keeps your files matching my
  > instructions exactly and avoids syntax-conversion mistakes. If your Android Studio version does
  > not offer this dropdown at all, tell me and I will give you `.kts` versions instead.

### 3.4 Wait for the first Gradle sync

After clicking **Finish**, Android Studio opens the project and starts downloading Gradle and the
Android Gradle Plugin. The status bar at the bottom shows **"Gradle: Downloading…"** /
**"Gradle sync in progress…"**.

**This can take 2–15 minutes on the first ever project and requires a working internet connection.**
Do not click anything until the bottom status bar is idle and the **Build** tab shows
`BUILD SUCCESSFUL`.

---

## 4. Files Android Studio creates (verify these exist)

Switch the Project panel dropdown (top-left of the file tree) from **Android** to **Project** at
least once so you can see the real folders. You should have:

```
SmartPrescriptionAssistantBD/
├── app/
│   ├── build.gradle                     <-- module-level (we edit this in STEP 2)
│   ├── proguard-rules.pro
│   └── src/
│       ├── main/
│       │   ├── AndroidManifest.xml
│       │   ├── java/com/example/smartprescriptionassistantbd/
│       │   │   └── MainActivity.java    <-- .java, NOT .kt
│       │   └── res/
│       │       ├── drawable/
│       │       ├── layout/
│       │       │   └── activity_main.xml
│       │       ├── mipmap-*/
│       │       ├── values/
│       │       │   ├── colors.xml
│       │       │   ├── strings.xml
│       │       │   └── themes.xml
│       │       └── xml/
│       ├── androidTest/
│       └── test/
├── build.gradle                         <-- project-level (we edit this in STEP 2)
├── settings.gradle
├── gradle.properties
├── local.properties                     <-- machine specific, never commit this
├── gradle/
│   ├── libs.versions.toml               <-- may or may not exist, depends on AS version
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
└── gradlew / gradlew.bat
```

### ✅ Self-check before moving on

Run through this list. **Every single one must be true.**

- [ ] There is a file `MainActivity.java` — the extension is `.java`, **not** `.kt`.
- [ ] There is **no** `.kt` file anywhere under `app/src/main/java/`.
- [ ] There is a file `app/src/main/res/layout/activity_main.xml`.
- [ ] The folder path is `java/com/example/smartprescriptionassistantbd/` exactly.
- [ ] `MainActivity.java` does **not** contain the words `setContent`, `@Composable`, or
      `androidx.compose`.
- [ ] Your build files are named `build.gradle`, not `build.gradle.kts`.

If any checkbox fails, **delete the project folder and redo section 3** — it is much faster than
trying to convert it later.

---

## 5. Contents of the generated files

These are generated **by Android Studio**, not written by you. Compare yours against these to
confirm the template was correct. Small differences (theme name, a comment) are fine.

### 5.1 `app/src/main/java/com/example/smartprescriptionassistantbd/MainActivity.java`

```java
package com.example.smartprescriptionassistantbd;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }
}
```

> Older Android Studio versions generate a shorter version without the `EdgeToEdge` lines.
> **Both are fine.** In STEP 3 we replace this file completely with the splash-screen logic.

### 5.2 `app/src/main/res/layout/activity_main.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

### 5.3 `app/src/main/AndroidManifest.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.SmartPrescriptionAssistantBD"
        tools:targetApi="31">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

> Note: there is **no** `package="..."` attribute in the modern manifest. The package now lives in
> `app/build.gradle` as `namespace` and `applicationId`. That is correct — do not add it back.

---

## 6. Gradle dependencies required for this step

**None.** We add every dependency (Firebase, ML Kit, Room, Material) in **STEP 2**, after you tell me
your SDK versions. Leave `app/build.gradle` untouched for now.

## 7. AndroidManifest changes required for this step

**None.** The generated manifest is correct as-is.

## 8. Firebase Console changes required for this step

**None.** Firebase setup happens in **STEP 5**, with full click-by-click instructions.

---

## 9. How to run and test

### Option A — Android Emulator

1. Menu **Tools → Device Manager**.
2. Click **+ → Create Virtual Device**.
3. Select **Phone → Pixel 6** → **Next**.
4. Pick a system image — choose one with **API 34** or **API 35** and click the ⬇ **Download** icon
   next to it. Wait for the download, then **Next → Finish**.
5. Close Device Manager. In the top toolbar device dropdown, select **Pixel 6 API 34**.
6. Press the green **Run ▶** button (or `Shift + F10`).

### Option B — Real Android phone (faster, recommended)

1. On the phone: **Settings → About phone → tap "Build number" 7 times** to unlock Developer options.
2. **Settings → System → Developer options → enable "USB debugging"**.
3. Connect the phone by USB, tap **Allow** on the "Allow USB debugging?" dialog.
4. The phone appears in the Android Studio device dropdown. Select it and press **Run ▶**.

## 10. Expected result

The app installs, launches, and shows a **white (or dark, depending on your system theme) screen with
`Hello World!` centered on it**. The app name shown under the launcher icon is
**Smart Prescription Assistant BD**.

The **Build** tab at the bottom shows:

```
BUILD SUCCESSFUL in 1m 12s
```

That is the whole goal of STEP 1. It looks like nothing, but it proves your toolchain, SDK, emulator
and Gradle all work — which means every later error is *our code*, not your setup.

---

## 11. Common errors and their exact fixes

### ❌ `MainActivity.kt` was created instead of `MainActivity.java`

**Cause:** You selected the **Empty Activity** (Compose) template.
**Fix:** Close the project (**File → Close Project**), delete the project folder from disk, and
redo section 3.2 selecting **Empty Views Activity**.

---

### ❌ The **Language** dropdown does not offer Java

**Cause:** Same as above — Compose templates are Kotlin-only, so the dropdown is hidden or locked.
**Fix:** Click **Previous** and choose **Empty Views Activity**.

---

### ❌ `Gradle sync failed: Could not resolve all files for configuration ':app:classpath'`

**Cause:** No internet, or a proxy/firewall blocking `dl.google.com` and `repo.maven.apache.org`.
**Fix:**
1. Confirm your internet works in a browser.
2. **File → Settings → Appearance & Behavior → System Settings → HTTP Proxy** → select
   **Auto-detect proxy settings** (or **No proxy** on a home connection).
3. Click **Try Again** in the yellow sync banner, or **File → Sync Project with Gradle Files**.

---

### ❌ `SDK location not found. Define location with sdk.dir in the local.properties file`

**Cause:** The Android SDK path is not registered.
**Fix:** **File → Settings → Languages & Frameworks → Android SDK**, note the
**Android SDK Location** path at the top, then open `local.properties` in the project root and set:

```properties
sdk.dir=C\:\\Users\\YourName\\AppData\\Local\\Android\\Sdk
```

(Windows needs the escaped backslashes. On macOS/Linux it is `sdk.dir=/Users/yourname/Library/Android/sdk`.)
Then **File → Sync Project with Gradle Files**.

---

### ❌ `Failed to install the following Android SDK packages as some licences have not been accepted`

**Fix:** Open a terminal in Android Studio (**View → Tool Windows → Terminal**) and run:

```
cd %LOCALAPPDATA%\Android\Sdk\cmdline-tools\latest\bin
sdkmanager --licenses
```

Press `y` for each prompt. On macOS/Linux:

```
cd ~/Library/Android/sdk/cmdline-tools/latest/bin
./sdkmanager --licenses
```

---

### ❌ `Unsupported class file major version 65` / `Unsupported Java version`

**Cause:** Gradle is using a JDK that the Android Gradle Plugin does not support.
**Fix:** **File → Settings → Build, Execution, Deployment → Build Tools → Gradle → Gradle JDK** →
select the bundled **jbr-17** (or **JetBrains Runtime 17**). Then **File → Invalidate Caches →
Invalidate and Restart**.

---

### ❌ Emulator shows a black screen or never boots

**Fix:**
1. **Tools → Device Manager** → click the ▾ next to your device → **Wipe Data**, then start it again.
2. If it still fails, enable hardware acceleration: on Windows install **Intel HAXM** / enable
   **Windows Hypervisor Platform** in *Turn Windows features on or off*.
3. Or just use a real phone (Option B above) — it is faster and avoids emulator problems entirely.

---

### ❌ `INSTALL_FAILED_INSUFFICIENT_STORAGE` on the emulator

**Fix:** **Device Manager → ▾ → Edit → Show Advanced Settings → Internal Storage**, raise it to
`4096 MB`, then **Wipe Data** and restart the emulator.

---

### ❌ Project folder name has no spaces (`SmartPrescriptionAssistantBD`)

**This is not an error.** Android Studio strips spaces from folder names. The app's display name is
controlled by `app_name` in `res/values/strings.xml`, which we will confirm in a later step.

---

## 12. What happens next

Once you confirm **"Step 1 works, I see Hello World"**, we move to:

**STEP 2 — Configure Gradle and dependencies**
(Material Components, Firebase Authentication, Google ML Kit Text Recognition, Room, ConstraintLayout,
Java 8+ desugaring, `viewBinding` decision, repositories, plugins.)

For that I need your exact environment — see the questions at the end of my message.
