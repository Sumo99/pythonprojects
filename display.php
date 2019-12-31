<?php
  // Original PHP code by Chirp Internet: www.chirp.com.au
  // Please acknowledge use of this code by including this header.
  $limit=100;
  function getImages($dir)
  {
    // array to hold return value
    $retval = [];

    // add trailing slash if missing
    if(substr($dir, -1) != "/") {
      $dir .= "/";
    }
    $filecount=0;
    // full server path to directory
    $fulldir = "{$_SERVER['DOCUMENT_ROOT']}/$dir";
    $retval=glob($fulldir."*.jpg");
    usort($retval, create_function('$a,$b', 'return filemtime($a)<filemtime($b);'));
    return $retval;
}
  $images = getImages("files");
  $img_count=count($images);
  $max_pages = ceil($img_count / $limit);
  if(isset($_GET["page"])){
    $show = array_slice($images, $limit * intval($_GET["page"]) - 1, $limit);
  }
  else{
    $show=array_slice($images, 0, 100);
  }

 // display on page
  echo" <meta http-equiv=\"refresh\" content=\"30\"/>";
  echo "<h1 style='text-align:center' > There are {$img_count} images </h1>";
  foreach($show as $img) {
    $img_path="/files/".basename($img);
    echo "<img class=\"photo\" src=\"{$img_path}\"  alt=\"\" style=\"margin-left: 5%;\" >\n";
  }
  echo("<br><br><br>");
   if(isset($_GET["page"])){

 if($_GET['page'] > 1){
    $prev_link = '<a href="?page='.($_GET['page']-1).'" > <p style="text-align:center"> previous </p> </a>';
    echo($prev_link);
 }
 if($_GET['page'] < $max_pages){
    $next_link = '<a href="?page='.($_GET['page']+1).'"  >  <p style="text-align:center"> next </p> </a>';
    echo($next_link);
 }
}
else{ //deal with the very first page
    $next_link = '<a href="?page=2" > <p style="text-align:center"> next </p> </a>';
    echo($next_link);
}

?>
