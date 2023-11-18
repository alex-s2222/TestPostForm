def find_matching_template(cursor, data) -> str | None:
    for document in cursor:
        #получаем ключи формы и удаляем ненужные
        template_fields = set(document.keys()) - {'name'} - {'_id'} 
        print("TEMPLATE",template_fields)
        
        data_fields = set(data.keys())
        print("DATA",data_fields)

        #проверяем на одинаковые ключи
        if data_fields.issuperset(template_fields):
            print("GOGOGO")
            # проверяем на одинаковое значение
            valid = all(__check_value(document[field], data[field]) for field in template_fields)
            if valid:
                return document['name']
    return None



def __check_value(template, data) -> bool:
    if template == data:
        return True
        