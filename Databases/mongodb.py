
import pymongo

mongoimport --db mongodata --collection slack_messages --file output.json --jsonArray

{
  "workspace_id": "string",
  "channel_id": "string",
  "user_id": "string",
  "message_id": "string",
  "timestamp": "datetime",
  "content": "string",
  "type": "string",  // message, reply, reaction, etc.
  "reply_to": "string",  // message_id of the parent message for replies
  "reactions": [
    {
      "emoji": "string",
      "users": ["string"]
    }
  ]
}



// Messages Collection
{
  "_id": ObjectId("unique_id"),
  "workspace_id": "workspace_1",
  "channel_id": "channel_123",
  "user_id": "user_456",
  "message_id": "msg_789",
  "timestamp": ISODate("2023-12-01T12:00:00.000Z"),
  "content": "Hello, world!",
  "type": "message",
  "reply_to": null,
  "reactions": [
    {
      "emoji": ":thumbsup:",
      "users": ["user_789", "user_012"]
    }
  ]
}
