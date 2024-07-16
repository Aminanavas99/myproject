# from django import template
# register = template.Library()

# # register=template.Library

# def chunks(list_data,chunk_size):
#     chunk=[]
#     i=0
#     for data in list_data:
#         chunk.append(data)
#         i+=1
#         if i==chunk_size:
#             yield chunk
#             chunk=[]
#     yield chunk


from django import template

register = template.Library()

@register.filter
def chunks(value, chunk_size):
    """Splits a list into chunks of specified size."""
    try:
        chunk_size = int(chunk_size)
        return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
    except (ValueError, TypeError):
        return value  # In case of invalid input, return the original value

        