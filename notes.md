#python setup
python -m venv env
source env/bin/activate
pip install Flask Flask-Cors
touch app.py

#Front End

##
npm install -g @vue/cli-init
vue init webpack client
1. runtime + compiler
2. vue-router yes
3. ESLint yes
4. ESLint preset Airbnb
5. unit tests no
6. e2d no
7. Run npm install? yes, npm.
## axios http calls
- npm install axios
## styles
- npm install bootstrap@4


npm run dev

# Ping.vue content
## add component Ping.vue
- template
- script
## get ping from Flask
- methods: { getPing() {
  - axios.get(path)
  - .then( res=>{this.msg=res.data} )
  - .catch(error=>{console.error(error)}) }}
- created(){ run getPing() }

## main.js
