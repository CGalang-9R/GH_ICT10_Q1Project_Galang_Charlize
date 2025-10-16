from pyscript import display, document

has_delivery = True
business_hours = '9:00AM - 6:00PM'
common_allergens = ['dyes', 'synthetic-fibers', 'dust mites', 'formaldehyde']
tax_rate = 0.15

display (f'We do have delivery! {has_delivery}!', target='delivery')

display (f'We are open from {business_hours}', target='hours')

display (f'Common allergens: {common_allergens[0]}, {common_allergens[1]}, {common_allergens[2]}, and {common_allergens[3]}. But do not worry! Our products are hypoallergenic.', target='allergens')

display (f'Tax rate: {tax_rate}', target='taxrate')