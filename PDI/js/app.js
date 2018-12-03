var app = angular.module('app', []);
app.controller('PdiCtrl', function($scope,$http) {
    $scope.init = false;
    $scope.ip = "images/img0.png";
    $scope.ita = "images/img0.png";
    $scope.iut = "images/img0.png";
    $scope.images = [];
    $scope.images.push("Imagem Original");
    $scope.qtd = 0;
    $scope.ut = null;
    $scope.tr = "Original";
    $scope.options = [
        "Gaussian Blur",
        "Median Blur",
        "Opening Filter",
        "Closing Filter",
        "Gradient Filter",
        "Laplacian",
        "Sobel",
        "Canny Edge Detection",
        "Histograms Equalization",
        "Hough Lines",
        "Remove Background",
        "Water shed ",
        "Tresh binary",
        "Tresh Otsu"
    ];

    $scope.add = function() {
        $scope.init = true;
    }

    $scope.call = function(name){
        $scope.qtd++;
        name=name.split(' ')[0];
        data = {name: name ,qtd:$scope.qtd , v1: 100, v2: 200};
        $http.post("php/haarcascade.php",data).then(function(){
            if($scope.tr != null && $scope.tr != "Original"){
                $scope.ut = $scope.tr;
                $scope.iut = $scope.ita;
            }
            $scope.tr = name;
            $scope.images.unshift(name);
            
            $scope.ita = "images/img"+$scope.qtd+".png";
        });
        
    };

    $scope.hc = function()
    {
        
        $http.post("php/haarcascade.php",data);
        
    }


});