# OCR Verse

OCR Verse is a Streamlit-based app for extracting text from PDFs and images using Mistral OCR. It supports input via
document URLs, file uploads, and image URLs. The extracted text is displayed in an expandable section for easy viewing.

Access the application [here](https://ocrverse.streamlit.app/).

## Installation

1. Checkout the GitHub repo.

```shell
gh repo clone lavvsharma/ocr_verse 
```

2. Install the required dependency

```shell
pip install .
```

3. Run the streamlit application

```shell
streamlit run OcrVerse.py
```

## Future scope

The app aims to integrate multiple OCR models, bringing them together in one platform for easy testing and comparison.
Additionally, users will be able to configure their own API keys, providing more flexibility and customization for
different OCR services.

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain
backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please
   open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://github.com/lavvsharma/ocr_verse/issues) with
questions, bugs, or suggestions.

## Requirements

Python 3.12 or higher.
