#
# Copyright (C) 2022 Teracube-Inc
#

# For use with LineageOS builds only.

# Set OTA property for emerald target.
ifeq ($(PRODUCT_DEVICE),emerald)
PRODUCT_PROPERTY_OVERRIDES += lineageos.updater.uri=https://raw.githubusercontent.com/teracube-mt6765-devs/platform_releases/master/updates/lineage-18.1-emerald.json
else
PRODUCT_PROPERTY_OVERRIDES += lineageos.updater.uri=https://raw.githubusercontent.com/teracube-mt6765-devs/platform_releases/master/updates/lineage-18.1-2e.json
endif
