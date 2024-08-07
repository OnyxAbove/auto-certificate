from fillpdf import fillpdfs

def main():
    form_fields = list(fillpdfs.get_form_fields('form.pdf').keys())

    name = input("Enter the recipient's name: ")
    reason = input("Enter the reason for the Thank You card: ")

    data_dict = {
        form_fields[0]: str(name),
        form_fields[1]: str(reason),
}

    fillpdfs.write_fillable_pdf('form.pdf', 'ty.pdf', data_dict, True)
    fillpdfs.flatten_pdf('ty.pdf', 'ty.pdf', as_images=False)

if __name__ == '__main__':
    main()