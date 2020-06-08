IMG_DIR := ./images

INPUTS := $(wildcard $(IMG_DIR)/*.png)
OUTPUTS := $(patsubst $(IMG_DIR)/%.png,$(IMG_DIR)/%.webp,$(INPUTS))

compress-images: $(OUTPUTS)

$(IMG_DIR)/%.webp: $(IMG_DIR)/%.png
	cwebp -q 85 $< -o $@

clean:
	rm -f $(OUTPUTS)

all: clean webp
