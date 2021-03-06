namespace foo {

    @doc("Essential information about a pet.")
    class Pet {

        @doc("The id of the pet.")
        int id;

        @doc("The name of the pet.")
        String name;

        @doc("The tag associated with the pet.")
        String tag;
    }

    @service("http://example.org/petstore")
    @doc("The PetStore service interface.")
    interface PetStore {

        @doc("Find a pet based upon its id.")
        @query Pet findPet(int id);

        @doc("Get an optionally limited set of pets based on a list of tags.")
        @query List<Pet> findPets(List<String> tags = null, int limit = null);

        @doc("Create a new pet.")
        @operation Pet createPet(String name, String tag = null);

        @doc("Delete a pet based on its id.")
        @operation void deletePet(int id);

    }

}
