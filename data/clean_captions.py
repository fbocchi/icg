import pandas as pd
import string

# Legge il file
df = pd.read_csv(
    "Flickr8k/Flickr8k_text/Flickr8k.token.txt",
    sep="\t",
    header=None,
    names=["image", "caption"]
)

images = []
captions = []

for _, row in df.iterrows():

    # ID immagine (senza .jpg e senza #0, #1, ...)
    image = row["image"].split("#")[0]
    image = image.replace(".jpg", "")

    # Standardizzazione caption
    caption = row["caption"].lower()

    for p in string.punctuation:
        caption = caption.replace(p, "")

    caption = " ".join([w for w in caption.split() if len(w) > 1])

    images.append(image)
    captions.append(caption)

# Nuovo DataFrame
df_new = pd.DataFrame({
    "image": images,
    "caption": captions
})

# Salva il CSV
df_new.to_csv("captions.csv", index=False)

print(df_new.head())