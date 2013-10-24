drop table if exists images;
create table images (
  image_url text not null,
  image_name text not null,
  image_tags text not null
);