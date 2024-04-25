# https://www.amazon.com/dp/B07BN217QG

from DrissionPage import WebPage

wp = WebPage()
wp.set.load_mode.eager()
wp.get('https://www.amazon.com/dp/B07BN217QG')
name = wp.ele('#productTitle').text
price = wp.ele('.a-spacing-none a-text-left a-size-mini twisterSwatchPrice').text
size = wp.ele('.a-spacing-small po-digital_storage_capacity').text
interface = wp.ele('.a-spacing-small po-hard_disk.interface').text
ssdtype = wp.ele('.a-spacing-small po-installation_type').text
# print(name, price, size, interface, ssdtype)



