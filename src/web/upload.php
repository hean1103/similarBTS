<?php
    # 저장될 파일
    $uploadfile = $_FILES['upload'] ['name'];
    # 저장 경로
    $path = "TEST/".$uploadfile;

    # 임시파일 -> 저장 경로로 저장
    move_uploaded_file($_FILES['upload']['tmp_name'],$path);
?>