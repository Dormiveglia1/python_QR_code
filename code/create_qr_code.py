import qrcode
from PIL import ImageColor

def create_qr_code(link, fill='black', back='white', version=1, box_size=10, border=5, error_correction='M', filename='qr.png'):
    # Error correction options
    # Allows QR codes to be read correctly even when partially damaged
    error_dict = {
        'L': qrcode.constants.ERROR_CORRECT_L,  # About 7% of errors can be corrected.
        'M': qrcode.constants.ERROR_CORRECT_M,  # About 15% of errors can be corrected.
        'Q': qrcode.constants.ERROR_CORRECT_Q,  # About 25% of errors can be corrected.
        'H': qrcode.constants.ERROR_CORRECT_H,  # About 30% of errors can be corrected.
    }

    # Convert color names or RGB strings to a PIL-compatible color
    def get_color(color_str):
        try:
            # If the input is in RGB format (e.g., "rgb(255,0,0)")
            if color_str.startswith('rgb'):
                rgb_values = color_str.strip('rgb()').split(',')
                return tuple(int(val) for val in rgb_values)
            # Otherwise, assume it's a named color
            return ImageColor.getrgb(color_str)
        except ValueError:
            # Fallback color if the input is invalid
            return (0, 0, 0)  # Default to black
        
    fill_color_pil = get_color(fill)
    back_color_pil = get_color(back)

    # Create QR code instance with dynamic parameters
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_dict[error_correction],
        box_size=box_size,
        border=border,
    )
    
    # Add data to QR code
    qr.add_data(link)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=fill, back_color=back)
    
    # Save the image to a file
    img.save(filename)
    return img

# Example of function call
# create_qr_code('https://github.com/Dormiveglia1', fill='red', back='yellow', version=5, box_size=10, error_correction='H')
