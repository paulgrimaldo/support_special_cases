'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  GET_CAREERS_API_URL: '"http://localhost:8000/api/v1/careers"',
  GENERATE_DOCUMENTATION_API_URL: '"http://localhost:8000/api/v1/generate-documentation"'
})
