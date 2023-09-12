<h1 align="center">
  <🧿> Piñata Vision
</h1>

<img src="https://github.com/Rakioth/PinataVision/assets/75569411/a9ce8a46-808d-4cfb-8fe9-32ae93eca38c" alt="Rare Logo" align="left" width="192"/>

## Project Overview

Piñata Vision is a feature of Viva Piñata: Trouble in Paradise.

You can scan a Piñata Vision card with the **Xbox LIVE Vision** camera to import its item into the game.

Special thanks to Peter Jensen for creating the original PV Creator for iOS and sharing the [pv-decoder](https://github.com/pinatavision/pv-decoder) repository.

<br/>

## 📦 Usage

Decoder script for identifying data encoded in a Piñata Vision barcode.

```bash
python pv_decoder.py <input_file> [-d]
```

Encoder script for generating Piñata Vision barcodes from decoded data.

```bash
python pv_encoder.py <input_file> [-d]
```

## 🃏 Custom Cards

[PV Creator](https://play.google.com/store/apps/details?id=com.raks.pvcreator) is an Android application that simplifies the creation of custom Piñata Vision cards. All cards generated using this app are free to use, and immediately reusable.