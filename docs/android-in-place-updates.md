# Android in-place update signing

The app ID is fixed at `com.shatteredrealms.next`. Android permits installing a newer APK over an existing version **only** when the installed and new APK signatures match and the new version code is higher.

The previous temporary debug APKs may have used disposable build-runner debug keystores. Those are not a reliable update channel. The Android workflow now **refuses to export** without these permanent repository Actions secrets:

- `ANDROID_KEYSTORE_BASE64`: base64 of the **private** .jks keystore file (one continuous line).
- `ANDROID_KEYSTORE_PASSWORD`: password used when the keystore was created.
- `ANDROID_KEY_ALIAS`: alias of the private key in that keystore.

Create the keystore only once, save a secure backup, and do not commit the keystore, its base64, or any password to GitHub. To create a test signing identity (Java 17 required):

```bash
keytool -genkeypair -v -keystore shattered-next.jks -alias shattered-next -keyalg RSA -keysize 3072 -validity 10000 -storepass 'CHOOSE_A_STRONG_PASSWORD' -keypass 'CHOOSE_A_STRONG_PASSWORD' -dname 'CN=Shattered Realms Next, OU=Development, O=Shattered Realms, C=US'
base64 -w 0 shattered-next.jks > keystore_base64.txt
```

Configure secrets under **Settings → Secrets and variables → Actions → New repository secret** for the `shattered-realms-next` repository. Do not upload `keystore_base64.txt` to the repository. Use its contents *only* for the GitHub secret.

The workflow exports **release-signed APKs with the same permanent key** and increments `version/code` using the workflow's run number. Keep the same signing secrets across future builds.

**One-time transition:** If the app already on the phone was signed with a different debug key, Android cannot install the newly release-signed APK over it. Export/backup any game data first, uninstall the old test build once, then install the first permanently signed build. Every subsequent higher-version build can install over it without uninstalling.

These updates are **install-over updates**, not automatic in-app downloads. The user still downloads and opens the next APK. In-app OTA updates require a separate update distribution implementation.
