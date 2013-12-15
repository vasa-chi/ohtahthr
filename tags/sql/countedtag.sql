CREATE OR REPLACE FUNCTION set_tag_count_on_insert() RETURNS TRIGGER AS $$
BEGIN
/* Надо найти тег, для кот. создано обращение и увеличить его count в 1*/
 UPDATE public.tags_countedtag SET count = count + 1 where id = NEW.tag_id;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION set_tag_count_on_delete() RETURNS TRIGGER AS $$
BEGIN
/* Надо найти тег, для кот. создано обращение и уменьшить его count в 1*/
 UPDATE public.tags_countedtag SET count = count - 1 where id = OLD.tag_id;
RETURN OLD;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS on_tag_add ON public.tags_countedtagthrough;
CREATE TRIGGER on_tag_add  AFTER INSERT ON public.tags_countedtagthrough
 FOR EACH ROW EXECUTE PROCEDURE set_tag_count_on_insert();
DROP TRIGGER IF EXISTS on_tag_delete ON public.tags_countedtagthrough;
 CREATE TRIGGER on_tag_delete BEFORE DELETE ON public.tags_countedtagthrough
 FOR EACH ROW EXECUTE PROCEDURE set_tag_count_on_delete();