function test(my_park) {
    var mapOptions = {
            // y좌표 다음 x좌표(WGS84 기준)
            center: new naver.maps.LatLng(my_park.LATITUDE, my_park.LONGITUDE),
            // 18 = 30m, 17 = 50m (휠단위로 1씩 변화)
            zoom: 18
    }

    var map = new naver.maps.Map('map', mapOptions)
}

function detail_ajax(area_num) {
    // javascript의 객체는 => {key : value, key : value, ...} 형태
    $.ajax({
        async : true,    // 비동기 방식의 호출(default)
        url : "http://openapi.seoul.go.kr:8088/6a6250617970617232376c4f505871/json/SearchParkInfoService/1/132/" + area_num,  // 호출할 url
        data : {
        },   // 서버 프로그램에게 넘겨줄 데이터들
        type : "GET",
        timeout : 5000,   // 주어진 시간안에 결과가 안오면 query가 실패한 것으로 간주
        dataType : "json",   // 서버로 부터 받을 데이터 타입
        success : function(result) {
            park_list = result.SearchParkInfoService.row[0]
            test(park_list)
            $("#myParkname").html(park_list.P_PARK)
            $("#myParkaddr").html(park_list.P_ADDR)
            $("#myParkcontents").html(park_list.P_LIST_CONTENT)
            $("#myParkequip").html(park_list.MAIN_EQUIP)
            $(".mainImg").attr("src", park_list.P_IMG)
//            var msg = "http://map.naver.com/index.nhn/place?&searchCoord=&level=12&lng=" + park_list.LONGITUDE + "&lat="
//            + park_list.LATITUDE + "&pinTitle=" + park_list.P_PARK + "&pinType=SITE"
            var msg = "window.open(" + "'http://map.naver.com/?query=" + park_list.P_ADDR + "')"
            $("#my_map").attr("onclick", msg)
//            P_ADDR
//            http://map.naver.com/index.nhn?&searchCoord=&level=12&lng=126.8689146&lat=37.5082119&pinTitle=갈산공원&pinType=SITE&enc=b64
//            http://map.naver.com/?query=경기도성남시분당구불정로6
//            var img = $("<img />").attr("src", park_list.P_IMG)
//            $("tbody").append(img)
        },
        error : function(error) {
            alert("서버호출 실패")
        }
    })

}

