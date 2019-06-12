###############################################################################
# Author:      Alok R. Saboo
# Description:  This script takes the dark_sky forecast sensors and updates
#               their friendly_name to include the date and day.
#               https://github.com/arsaboo/homeassistant-config/blob/master/packages/weather.yaml
###############################################################################
forecast_entities = ["sensor.fforecast_1", "sensor.fforecast_2", "sensor.fforecast_3",
                     "sensor.fforecast_4","sensor.cforecast_1", "sensor.cforecast_2", "sensor.cforecast_3", "sensor.cforecast_4"] # "sensor.cforecast_5", "sensor.cforecast_6", "sensor.cforecast_7"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

triggeredEntity = data.get('entity_id')
# logger.warning("trigger is {}".format(triggeredEntity))
now = datetime.datetime.now()
today = now.weekday()

if triggeredEntity is None:
    for entity_id in forecast_entities:
        # copy it's state
        state = hass.states.get(entity_id)
        newState = state.state
        forecastdays = int(entity_id.split('_')[1])
        day = datetime.timedelta(days = forecastdays)
        forecastdate = now + day
        newEntityPicture = state.attributes.get('entity_picture')
        if today + forecastdays > 6:
            newDay = days[today + forecastdays - 7]
        else:
            newDay = days[today + forecastdays]
        # Set states
        hass.states.set(entity_id, newState, {
            'friendly_name': "{} ({}/{})".format(newDay, forecastdate.day, forecastdate.month),
            'entity_picture': newEntityPicture,
        })
else:
    state = hass.states.get(triggeredEntity)
    newState = state.state
    forecastdays = int(triggeredEntity.split('_')[1])
    day = datetime.timedelta(days = forecastdays)
    forecastdate = now + day
    newEntityPicture = state.attributes.get('entity_picture')
    if today + forecastdays > 6:
        newDay = days[today + forecastdays - 7]
    else:
        newDay = days[today + forecastdays]
    # Set states
    hass.states.set(triggeredEntity, newState, {
        'friendly_name': "{} ({}/{})".format(newDay, forecastdate.month, forecastdate.day),
        'entity_picture': newEntityPicture,
})
