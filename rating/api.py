# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from ohthathr.api import TYPE_MATCH_MAP
from models import RatedByUser


def rating_manipulation(data):
    """Инкрементация/декрементация рейтинга для объекта.

       Args:
            data: объекта для инкримента рейтинга. Словарь.
                  object_pk: pk объекта, для кот. инк/дек. рейтинг;
                  item_type: См. TYPE_MATCH_MAP;
                  type: тип действия. 0 - декремент, 1 - инкремент;
                  user: Пользователь, совершивший манипуляцию с рейтингом;

    """
    model = TYPE_MATCH_MAP[data["item_type"]]
    ct = ContentType.objects.get_for_model(model)
    rated_by_qs = RatedByUser.objects.filter(object_id=data["object_pk"], content_type=ct, user=data["user"])
    # если пользователь УЖЕ делал инкремент или декремент комменту, т.е. такое же действие.
    if rated_by_qs.filter(action_type=data["type"]).exists():
        raise Http404()
    else:
        if rated_by_qs.exists():
            # если пользователь что-то делал с рейтингом объекта
            rated_by_qs.update(action_type=data["type"])
        else:
            RatedByUser.objects.create(object_id=data["object_pk"], content_type=ct,
                                       user=data["user"], action_type=data["type"])
        try:
            object = model.objects.select_for_update().get(pk=data["object_pk"])
            if data["type"] == 0:
                object.rating -= 1
            elif data["type"] == 1:
                object.rating += 1
            object.save(update_fields=["rating"])
        except model.DoesNotExists:
            raise Http404()
        #TODO: notify
        return object.rating