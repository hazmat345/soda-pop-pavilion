
versionService.$inject = ['$http'];
export default function versionService($http) {
  return {
    errorMap: {
      'empty': {
        'solutions' : [
          {
            problem: 'Request was removed',
            description: 'INFO-type requests are removed after several minutes',
            resolution:  'Go back to the list of all requests'
          },
          {
            problem: 'ID is Incorrect',
            description: 'The ID Specified is incorrect. It does not refer to a valid request',
            resolution:  'Go back to the list of all requests'
          }
        ]
      }
    },

    getVersionInfo: function() {
      return $http.get('version');
    }
  }
};
