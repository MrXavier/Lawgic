'use client'

import { useState, useRef } from 'react'
import { useChat } from 'ai/react'
import { Send } from 'lucide-react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { toast } from "@/components/ui/use-toast"

export default function SimplifiedLegalChat() {
  const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat()

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    handleSubmit(e)
  }

  return (
    <div className="flex flex-col h-screen max-w-2xl mx-auto p-4">
      <ScrollArea className="flex-1 p-4 rounded-md border mb-4">
        {messages.map(m => (
          <div
            key={m.id}
            className={`mb-4 ${
              m.role === 'user' ? 'text-blue-600 text-right' : 'text-gray-600'
            }`}
          >
            <span className="font-bold">{m.role === 'user' ? 'You: ' : 'AI: '}</span>
            {m.content}
          </div>
        ))}
        {isLoading && (
          <div className="text-gray-400 animate-pulse">AI is typing...</div>
        )}
      </ScrollArea>
      <form onSubmit={onSubmit} className="flex space-x-2">
        <Input
          value={input}
          onChange={handleInputChange}
          placeholder="Ask a legal question..."
          className="flex-1"
        />
        <Button type="submit" disabled={isLoading}>
          <Send className="h-4 w-4 mr-2" />
          Send
        </Button>
      </form>
    </div>
  )
}