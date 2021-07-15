
class Container:
    def __init__(self, client, dictionary):
        self.client = client
        self.dictionary = dictionary

    @classmethod
    def from_ps(cls, client, dictionary, **kwargs):
        """
        Construct a container object from the output of GET /containers/json.
        """
        name = get_container_name(dictionary)
        if name is None:
            return None

        new_dictionary = {
            'Id': dictionary['Id'],
            'Image': dictionary['Image'],
            'Name': '/' + name,
        }
        return cls(client, new_dictionary, **kwargs)


    @property
    def name(self):
        return self.dictionary['Name'][1:]


    @property
    def ports(self):
        return None


def get_container_name(container):
    if not container.get('Name') and not container.get('Names'):
        return None
    # inspect
    if 'Name' in container:
        return container['Name']
    # ps
    shortest_name = min(container['Names'], key=lambda n: len(n.split('/')))
    return shortest_name.split('/')[-1]
