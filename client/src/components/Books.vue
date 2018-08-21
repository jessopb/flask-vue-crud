<template>
  <div class="container">
    <div class="jumbotron">
      <h1>Books</h1>
      <button type="button"
        class="btn btn-primary"
        name="button"
        v-b-modal.book-modal-id>Add Book</button>
      <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Title</th>
          <th scope="col">Author</th>
          <th scope="col">Read?</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(book, index) in books" :key="index" >

          <td>{{book.index}}</td>
          <td>{{book.title}}</td>
          <td>{{book.author}}</td>
          <td>{{book.read}}</td>
          <td><button class="btn btn-warning" name="button">Update</button>
            <button class="btn btn-danger" name="button">Delete</button></td>

        </tr>
      </tbody>
    </table>
    </div>
      <b-modal ref="addBookModal"
         id="book-modal-id"
         title="Add a new book"
         hide-footer>
        <b-form @submit="onSubmit"
                @reset="onReset"
                class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addBookForm.author"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read"
                                 id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit"
                  variant="primary">Submit</b-button>
        <b-button type="reset"
              variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Books',
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';

      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read,
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
button{
  margin: auto;
}
</style>
