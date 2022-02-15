#
# Copyright (C) 2022 Teracube-Inc
#

# For use with LineageOS builds only.

# Set OTA property for emerald target.
ifeq ($(PRODUCT_DEVICE),emerald)
PRODUCT_PROPERTY_OVERRIDES += lineageos.updater.uri=https://raw.githubusercontent.com/teracube-mt6765-devs/releases/master/los11-emerald.json
else
PRODUCT_PROPERTY_OVERRIDES += lineageos.updater.uri=https://raw.githubusercontent.com/teracube-mt6765-devs/releases/master/los11-2e.json
endif
